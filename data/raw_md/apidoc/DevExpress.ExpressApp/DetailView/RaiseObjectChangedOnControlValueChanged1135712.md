---
uid: DevExpress.ExpressApp.DetailView.RaiseObjectChangedOnControlValueChanged
name: RaiseObjectChangedOnControlValueChanged
type: Property
summary: Specifies whether the @DevExpress.ExpressApp.IObjectSpace.ObjectChanged event should occur each time you modify a control value in a DetailView (see the [BC5087](https://supportcenter.devexpress.com/ticket/details/bc5087/core-the-iobjectspace-objectchanged-event-is-not-raised-in-response-to-the-editor-s) breaking change).
syntax:
  content: |-
    [Browsable(false)]
    public bool RaiseObjectChangedOnControlValueChanged { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if the @DevExpress.ExpressApp.IObjectSpace.ObjectChanged event should occur each time you modify a control value in the DetailView; otherwise, **false**. The default value is **false**.'
seealso:
- linkId: DevExpress.ExpressApp.DetailView.DefaultRaiseObjectChangedOnControlValueChanged
---
Generally, you do not need to use this property.
