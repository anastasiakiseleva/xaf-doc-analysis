---
uid: DevExpress.ExpressApp.XafApplication.EditorFactory
name: EditorFactory
type: Property
summary: Provides access to the application's Editors Factory, which is used to load [View Items](xref:112612) and [List Editors](xref:113189) to the [Application Model](xref:112580) and create them when needed.
syntax:
  content: |-
    [Browsable(false)]
    public IEditorsFactory EditorFactory { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Editors.IEditorsFactory
    description: An **IEditorsFactory** object that represents the current application's Editors Factory.
seealso: []
---
Generally, you do not need to use this property. It is for internal use only.