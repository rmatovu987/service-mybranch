import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { FormValidatorComponent } from '../components/components/form-validator/form-validator.component';
import { FormControlModel } from '../components/models/form.model';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignupComponent extends FormValidatorComponent implements OnInit {
  form!: FormGroup;
  isLoading: boolean = false;

  constructor(private fb: FormBuilder) {
    super();
  }

  override ngOnInit(): void {
    this.createForm();
  }

  signup() {
    console.log(this.form.value);
    if (this.form.valid) {
    } else {
      this.validateAllFormFields(this.form);
    }
  }

  createForm() {
      this.form = this.fb.group({
        email: new FormControlModel(
          {
            label: 'Email',
            name: 'email',
            placeholder: 'Email',
            icon: 'bi bi-person',
            type: 'text',
            value: '',
            validation: {
              required: 'Please enter your email!',
            },
          },
          '',
          [Validators.required]
        ),
        password: new FormControlModel(
          {
            label: 'Password',
            name: 'password',
            placeholder: '*******',
            icon: 'bi bi-shield-lock',
            type: 'password',
            value: '',
            validation: {
              required: 'Please enter your password.',
            },
          },
          '',
          [Validators.required]
        )
      });
  }
}
