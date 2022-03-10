import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { FormValidatorComponent } from '../components/components/form-validator/form-validator.component';
import { FormControlModel } from '../components/models/form.model';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent extends FormValidatorComponent implements OnInit {
  form!: FormGroup;
  isLoading: boolean = false;

  constructor(private fb: FormBuilder) {
    super();
  }

  override ngOnInit(): void {
    this.createForm();
  }

  login() {
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
      ),
      rememberMe: new FormControlModel(
        {
          label: 'Remember me',
          name: 'rememberMe',
          placeholder: '',
          icon: '',
          type: 'checkbox',
          value: '',
          validation: {},
        },
        '',
        []
      ),
    });
  }
}
