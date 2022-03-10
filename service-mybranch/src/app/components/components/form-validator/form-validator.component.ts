import { Component, OnInit, ViewChild } from '@angular/core';
import { FormControl, FormGroup, FormGroupDirective } from '@angular/forms';
import { FormControlModel, FormGroupModel } from '../../models/form.model';

@Component({
  selector: 'app-form-validator',
  templateUrl: './form-validator.component.html',
  styleUrls: ['./form-validator.component.scss']
})
export class FormValidatorComponent implements OnInit {
  @ViewChild(FormGroupDirective) formDirective!: FormGroupDirective;

  constructor() {}

  ngOnInit(): void {}

  public validateAllFormFields(formGroup: FormGroup) {
    Object.keys(formGroup.controls).forEach((field) => {
      const control = formGroup.get(field);
      if (control instanceof FormControl) {
        control.markAsTouched({ onlySelf: true });
      } else if (control instanceof FormGroup) {
        this.validateAllFormFields(control);
      }
    });
  }

  public unValidateAllFormFields(formGroup: FormGroup) {
    formGroup.reset();
    Object.keys(formGroup.controls).forEach((field) => {
      const control = formGroup.get(field) as FormControlModel | FormGroupModel;
      if (control instanceof FormControl) {
        control.markAsUntouched({ onlySelf: true });
        if (control.errorMessages != null) {
          control.errorMessages = [];
        }
      } else if (control instanceof FormGroup) {
        this.unValidateAllFormFields(control);
      }
    });
  }

  public validateFormFields(control: FormControlModel) {
    control.markAsTouched({ onlySelf: true });
  }

  public unValidateFormFields(control: FormControlModel) {
    control.markAsUntouched({ onlySelf: true });
        if (control.errorMessages != null) {
          control.errorMessages = [];
        }
  }
}
