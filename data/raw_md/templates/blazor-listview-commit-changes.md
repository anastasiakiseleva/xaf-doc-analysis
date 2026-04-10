If a Detail View contains a nested List View, a click on the **Save** button in the List View's in-line edit form does not save changes in that List View. These changes are applied only when you save the object associated with the root Detail View. To change this behavior, override the `AutoCommitChanges` property of the `ListEditorInplaceEditController`:

```csharp
public class CustomListEditorInplaceEditController : ListEditorInplaceEditController {
    protected override bool AutoCommitChanges => View.Id == "SomeBusinessObject_ListView" ? true : base.AutoCommitChanges;
}
```