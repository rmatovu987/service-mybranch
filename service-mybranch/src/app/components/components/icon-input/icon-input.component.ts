import { Component, Input, OnDestroy, OnInit } from '@angular/core';
import { FormControlModel } from '../../models/form.model';

@Component({
  selector: 'app-icon-input',
  templateUrl: './icon-input.component.html',
  styleUrls: ['./icon-input.component.scss']
})
export class IconInputComponent implements OnInit, OnDestroy {
  @Input() control!: FormControlModel;

  constructor() {}

  ngOnInit(): void {}

  ngOnDestroy(): void {
    this.control.unsubscribe();
  }

}
