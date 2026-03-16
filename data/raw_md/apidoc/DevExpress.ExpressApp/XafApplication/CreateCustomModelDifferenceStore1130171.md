---
uid: DevExpress.ExpressApp.XafApplication.CreateCustomModelDifferenceStore
name: CreateCustomModelDifferenceStore
type: Event
summary: Occurs when a storage for model differences is being created.
syntax:
  content: public event EventHandler<CreateCustomModelDifferenceStoreEventArgs> CreateCustomModelDifferenceStore
seealso: []
---
<!--check whether this member is relevant to Blazor, see note -->
The [Application Model](xref:112580)'s base content formed from the code can be changed via the [Model Editor](xref:112830). When the Application Model is loaded, the changes from the _Model.xafml_ file are superimposed on the content generated previously. To load the changes saved to the _Model.xafml_ file, a special storage is used. It finds this file near the executable file in the application project and load changes to the Application Model. For details, refer to the [Model Difference Storages](xref:403527) article.

If you need to store the _Model.xafml_ file in a custom resource (e.g., in a Web service or register), implement your own storage by inheriting from the `ModelDifferenceStore` abstract class. To make the system use your storage, handle the `CreateCustomModelDifferenceStore` event and set it for the handler's `Store` parameter. To prohibit the creation of the default storage object, set the handler's `Handled` parameter to `true`.

> [!NOTE]
> If you need to modify the mechanism of Application Model differences store in both an ASP.NET Core Blazor and Windows Forms application, you need to use an individual handler in the ASP.NET Core Blazor and Windows Forms application.

To see an example of using the `CreateCustomModelDifferenceStore` event, refer to the [How to: Store the Application Model Differences in the Database](xref:113698) topic. To use a custom storage for saving and loading an end-user's Application Model changes, handle the [XafApplication.CreateCustomUserModelDifferenceStore](xref:DevExpress.ExpressApp.XafApplication.CreateCustomUserModelDifferenceStore) event.