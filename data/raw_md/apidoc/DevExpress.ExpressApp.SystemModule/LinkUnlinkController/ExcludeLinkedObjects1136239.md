---
uid: DevExpress.ExpressApp.SystemModule.LinkUnlinkController.ExcludeLinkedObjects
name: ExcludeLinkedObjects
type: Property
summary: Specifies whether to exclude the objects that are already linked from the List View invoked by the [LinkUnlinkController.LinkAction](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.LinkAction).
syntax:
  content: public bool ExcludeLinkedObjects { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true` to exclude linked objects; otherwise, `false`.'
seealso: []
---
All the objects of the specified type are displayed in the invoked List View. If you do not want to display linked objects in the invoked List View, set this property to `true`. Note that if you enable this feature, all changes should be commited to a database before you invoke the List View. Otherwise, you may see unexpected records.
