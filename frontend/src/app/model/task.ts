import { Project } from './project';
import { Label } from './label';
import { GithubUser } from './github_user';
import { Milestone } from './milestone';

export interface Task {
  id: number;
  title: string;
  description: string;
  due_date: string;
  task_state: 'open' | 'in review' | 'in progress' | 'done';
  project: Project;
  labels: Array<Label>;
  milestones: Array<Milestone>;
  assignee: GithubUser;
  author: GithubUser;
  opened: boolean;
}
