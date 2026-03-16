---
uid: DevExpress.ExpressApp.ListView.RestoreFocusedObject
name: RestoreFocusedObject
type: Property
summary: Specifies whether XAF should restore focus after the object collection changes.
syntax:
  content: public bool RestoreFocusedObject { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true` if XAF should restore focus; otherwise, `false`.'
seealso: []
---
Set the `RestoreFocusedObject` property to `false` to prevent XAF from restoring the object focus when object collection changes. For instance, this can be useful when implementing [Web Style Row Selection in GridView](xref:711#web-style-row-selection-in-gridview).