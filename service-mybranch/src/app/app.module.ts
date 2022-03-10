import { NgModule } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CheckboxComponent } from './components/components/checkbox/checkbox.component';
import { IconInputComponent } from './components/components/icon-input/icon-input.component';
import { LandingPageComponent } from './landing-page/landing-page.component';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { FormValidatorComponent } from './components/components/form-validator/form-validator.component';


@NgModule({
  declarations: [
    AppComponent,
    LandingPageComponent,
    LoginComponent,
    SignupComponent,
    IconInputComponent,
    CheckboxComponent,
    FormValidatorComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    // FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
