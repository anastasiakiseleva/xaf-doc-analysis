---
uid: DevExpress.ExpressApp.Editors.ColumnsListEditor.PreventServerSideOperationsForNonPersistentMembers
name: PreventServerSideOperationsForNonPersistentMembers
type: Property
summary: Specifies whether server-side operations are prevented for non-persistent properties in the [Server, ServerView, InstantFeedback, and InstantFeedbackView](xref:113683) data access modes, or not.
syntax:
  content: public bool PreventServerSideOperationsForNonPersistentMembers { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true` if server-side operations are prevented for non-persistent properties in the `Server`, `ServerView`, `InstantFeedback`, and `InstantFeedbackView` List View data access modes, otherwise `false`. The default value is `true`.'
seealso: []
---
In server modes, grid controls perform operations like sorting, grouping, and filtering on the data store side to guarantee the best performance. Columns bound to non-persistent properties cannot be used for such server-based operations. The `PreventServerSideOperationsForNonPersistentMembers` property allows you to disable all server-based operations for non-persistent properties in the WinForms [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor) editor.

If this property is set to `true`, the following behavior is expected.

* The grid's Find Panel does not take non-persistent properties into account.
* The grid's Filter Editor does not display non-persistent properties in the properties tree.
* The grid's Auto Filter Row feature is not available for non-persistent columns.
* Grid column headers for non-persistent columns do not allow end-users to filter, sort or group.

You can change this property in the overridden `OnActivated` method of a custom [](xref:DevExpress.ExpressApp.ViewController`1) for a required ListView.
