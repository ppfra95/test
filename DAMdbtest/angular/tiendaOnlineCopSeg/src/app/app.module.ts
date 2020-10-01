import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RegisterCustomerComponent } from './register-customer/register-customer.component';
import { CustomersListComponent } from './customers-list/customers-list.component';
import { CustomerDetailsComponent } from './customer-details/customer-details.component';
import { LoginCustomerComponent } from './login-customer/login-customer.component';
import { SearchCustomersComponent } from './search-customers/search-customers.component';

@NgModule({
  declarations: [
    AppComponent,
    RegisterCustomerComponent,
    CustomersListComponent,
    CustomerDetailsComponent,
    LoginCustomerComponent,
    SearchCustomersComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
