---
uid: DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.AllowClear
name: AllowClear
type: Property
summary: Specifies whether or not a user can clear a value in the lookup editor.
syntax:
  content: |-
    [ModelBrowsable(typeof(AllowClearCalculator))]
    bool AllowClear { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, when a user can clear a value in the lookup editor; otherwise - **false**.'
seealso: []
---
By default, the **Clear** button is available in lookup editors (see [Reference (Foreign Key, Complex Type) Properties](xref:113572)).

![AllowClear](~/images/allowclear117368.png)

To hide this button, set the **AllowClear** property to **false** in the [Model Editor](xref:112582).

![AllowClear_ME](~/images/allowclear_me117369.png)