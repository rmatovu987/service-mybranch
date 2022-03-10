import {
  AbstractControlOptions,
  AsyncValidatorFn,
  FormControl,
  FormGroup,
  ValidatorFn
} from '@angular/forms';
import { Subject, Subscription } from 'rxjs';

export interface InputModel {
  label?: string;
  name: string;
  icon?: string;
  type: string;
  value: any;
  placeholder?: string;
  validation?: {};
  errorMessages?: Array<string>;
}

export class FormControlModel extends FormControl implements InputModel {
  label?: string;
  name: string;
  icon?: string;
  type: string;
  override value: any;
  placeholder?: string;
  validation?: any;
  errorMessages?: Array<string>;

  private sub!: Subscription;

  constructor(
    config: InputModel,
    formState: any = null,
    validatorOrOpts?: ValidatorFn | AbstractControlOptions | ValidatorFn[],
    asyncValidator?: AsyncValidatorFn | AsyncValidatorFn[]
  ) {
    super(formState, validatorOrOpts, asyncValidator);

    this.label = config.label;
    this.name = config.name;
    this.icon = config.icon;
    this.type = config.type;
    this.value = config.value;
    this.placeholder = config.placeholder;
    this.validation = config.validation;

    this.sub = this.touchedChanges.subscribe(() => {
      this.errorMessages = [];
      if (this.errors && (this.touched || this.dirty)) {
        Object.keys(this.errors).forEach((messageKey) => {
          if (this.validation[messageKey]) {
            this.errorMessages!.push(this.validation[messageKey]);
          }
        });
      }
    });
  }

  public touchedChanges: Subject<boolean> = new Subject<boolean>();

  override markAsTouched({ onlySelf }: { onlySelf?: boolean } = {}): void {
    super.markAsTouched({ onlySelf });

    this.touchedChanges.next(true);   
  }

  public unsubscribe(): void {
    this.sub.unsubscribe();
  }
}

export class FormGroupModel extends FormGroup implements InputModel {
  label?: string;
  name: string;
  icon?: string;
  type: string;
  override value: any;
  placeholder?: string;
  validation?: any;
  errorMessages?: Array<string>;

  private sub: Subscription;

  constructor(
    config: InputModel,
    formState: any = null,
    validatorOrOpts?: ValidatorFn | AbstractControlOptions | ValidatorFn[],
    asyncValidator?: AsyncValidatorFn | AsyncValidatorFn[]
  ) {
    super(formState, validatorOrOpts, asyncValidator);

    this.label = config.label;
    this.name = config.name;
    this.icon = config.icon;
    this.type = config.type;
    this.value = config.value;
    this.placeholder = config.placeholder;
    this.validation = config.validation;

    this.sub = this.touchedChanges.subscribe(() => {
      this.errorMessages = [];
      if (this.errors && (this.touched || this.dirty)) {
        Object.keys(this.errors).forEach((messageKey) => {
          if (this.validation[messageKey]) {
            this.errorMessages!.push(this.validation[messageKey]);
          }
        });
      }
    });
  }

  touchedChanges: Subject<boolean> = new Subject<boolean>();

  override markAsTouched({ onlySelf }: { onlySelf?: boolean } = {}): void {
    super.markAsTouched({ onlySelf });

    this.touchedChanges.next(true);   
  }
  
  public unsubscribe(): void {
    this.sub.unsubscribe();
  }
}
