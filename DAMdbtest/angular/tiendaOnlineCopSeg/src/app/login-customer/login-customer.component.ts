import { Component, OnInit, Input } from '@angular/core';

import { CustomerService } from '../customer.service';
import { Customer } from '../customer';

import { CustomersListComponent } from '../customers-list/customers-list.component';

@Component({
  selector: 'app-login-customer',
  templateUrl: './login-customer.component.html',
  styleUrls: ['./login-customer.component.css']
})
export class LoginCustomerComponent implements OnInit {

  email:string;
  password:string;
  // customer: Observable<Customer[]>;
  customer: Customer = new Customer();

  constructor(private dataService: CustomerService) { }

  ngOnInit() {
    this.email="";
    this.password="";
  }

  reloadData() {
    // this.customers = [];
    // this.dataService.loginCustomer(this.email,this.password)
    //   .subscribe(
    //     data => {
    //       console.log(data);
    //       this.customer = data;
    //     },
    //     error => console.log(error));
    this.dataService.loginCustomer(this.customer)
      .subscribe(
        data => {
          console.log(data);
          this.customer = data;
        },
        error => console.log(error));
  }

  onSubmit() {
    this.reloadData();
  }

}
