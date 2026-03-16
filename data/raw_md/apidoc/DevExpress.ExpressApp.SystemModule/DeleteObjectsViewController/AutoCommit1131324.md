---
uid: DevExpress.ExpressApp.SystemModule.DeleteObjectsViewController.AutoCommit
name: AutoCommit
type: Property
summary: Specifies whether to remove objects immediately.
syntax:
  content: public bool AutoCommit { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true** if objects are deleted from the database immediately; **false** if objects are deleted immediately from root Views, and deleted at the next committing of the changes collected by the Object Space, if the object(s) are from a nested View.'
seealso: []
---
By default, this property is set to **false**. So, objects from root Views are deleted immediately. However, objects from nested Views are marked as objects to be deleted. They are deleted during the next call of the [BaseObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.BaseObjectSpace.CommitChanges) method.