import { Component } from '@angular/core';
import { Link } from './link/link.model'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'angular-links-votes-app';
  links: Link[];

  constructor(){
    this.links = [];
  }

  addLink(title: HTMLInputElement, link: HTMLInputElement){
    this.links.push(new Link(title.value, link.value));
    title.value = '';
    link.value = '';
    return false;
  }
}
