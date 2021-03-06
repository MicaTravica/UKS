import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Milestone } from 'src/app/model/milestone';
import { Task } from 'src/app/model/task';
import { MilestoneService } from 'src/app/services/milestone.service';
import { TaskService } from 'src/app/services/task.service';

@Component({
  selector: 'app-details-milestone',
  templateUrl: './details-milestone.component.html',
  styleUrls: ['./details-milestone.component.css']
})
export class DetailsMilestoneComponent implements OnInit {

  public milestone: Milestone = { title: '', description: '', due_date: '', start_date: '', project: 0};
  public tasks: Task[] = [];
  public id: string;
  public projectId: string;
  constructor(private route: ActivatedRoute,
              private router: Router,
              private milestoneService: MilestoneService,
              private taskService: TaskService) { }

  ngOnInit() {
    const id = this.route.snapshot.params.id;
    this.id = id;
    this.projectId = this.route.snapshot.params.projectId;
    this.milestoneService.get(id).subscribe(
      (data: Milestone) => {
        this.milestone = data;
      }
    );

    this.taskService.getTasksByMilestone(id).subscribe(
      (data: Task[]) => {
        this.tasks = data;
      }
    );

  }

  openedNum() {
    let count = 0;
    for (const task of this.tasks) {
        if (task.opened) {
            count++;
        }
    }
    return count;
  }

  edit() {
    this.router.navigate(['/dashboard/home/' + this.projectId + '/' + this.projectId + '/milestone-new/' + this.id]);
  }

  newIssue() {
    this.router.navigate(['dashboard/home/' + this.projectId + '/' + this.projectId + '/issue-create']);
  }

  editIssue(task: Task) {
    this.router.navigate(['dashboard/home/' + this.projectId + '/' + this.projectId + '/issue-edit/' + task.id]);
  }
}
