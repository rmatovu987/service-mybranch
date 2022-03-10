import { Component, Input, OnInit } from '@angular/core';
import { FormControlModel } from '../../models/form.model';

@Component({
  selector: 'app-checkbox',
  templateUrl: './checkbox.component.html',
  styleUrls: ['./checkbox.component.scss']
})
export class CheckboxComponent implements OnInit {

  @Input() label: string | null = null;
  @Input() control!: FormControlModel;
  
  constructor() { }

  ngOnInit(): void {
  }

}
