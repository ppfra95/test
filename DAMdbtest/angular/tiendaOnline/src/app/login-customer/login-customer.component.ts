import { Component, OnInit } from '@angular/core';

import { CustomerService } from '../customer.service';
import { Customer } from '../customer';

@Component({
  selector: 'app-login-customer',
  templateUrl: './login-customer.component.html',
  styleUrls: ['./login-customer.component.css']
})
export class LoginCustomerComponent implements OnInit {

  email:string;
  password:string;
  customers: Customer[];

  constructor(private dataService: CustomerService) { }

  ngOnInit() {
    this.email="";
    this.password="";
  }

  reloadData() {
    this.customers = [];
    this.dataService.loginCustomer(this.email,this.password)
      .subscribe(customers => this.customers = customers);
  }

  onSubmit() {
    this.reloadData();
  }

}
