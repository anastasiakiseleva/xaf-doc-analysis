---
uid: DevExpress.ExpressApp.XafApplication.CreateCustomUserModelDifferenceStore
name: CreateCustomUserModelDifferenceStore
type: Event
summary: Occurs when a storage for end-user model differences is being created.
syntax:
  content: public event EventHandler<CreateCustomModelDifferenceStoreEventArgs> CreateCustomUserModelDifferenceStore
seealso: []
---
When the [Application Model](xref:112580) is loaded, the differences from modules (_Model.DesignedDiffs.xafml_ files) and the application project (_Model.xafml_ file) are superimposed on the base content generated from code. In addition, changes made by an end-user are saved to the _Model.User.xafml_ file and loaded as the topmost level when the Application Model is loaded. For details, refer to the [Model Difference Storages](xref:403527) article.

If you need to store end-user differences in another location (not in the _Model.User.xafml_ file), implement a custom storage by inheriting from the `ModelDifferenceStore` abstract class. To make the system use your storage, handle the `CreateCustomUserModelDifferenceStore` event and set it for the handler's `Store` parameter. To prohibit the creation of the default storage object, set the handler's `Handled` parameter to `true`.

To see an example of using the `CreateCustomUserModelDifferenceStore` event, refer to the [How to: Store the Application Model Differences in the Database](xref:113698) topic.

> [!NOTE]
> If you need to modify the mechanism of Application Model differences to store them both in an ASP.NET Core Blazor and Windows Forms application, you need to use an individual handler in the ASP.NET Core Blazor and Windows Forms application.