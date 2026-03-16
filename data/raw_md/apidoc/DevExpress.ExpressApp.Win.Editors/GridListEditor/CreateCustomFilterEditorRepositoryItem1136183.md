---
uid: DevExpress.ExpressApp.Win.Editors.GridListEditor.CreateCustomFilterEditorRepositoryItem
name: CreateCustomFilterEditorRepositoryItem
type: Event
summary: Occurs when creating a Filter Editor for the current Grid List Editor.
syntax:
  content: public event EventHandler<CreateCustomRepositoryItemEventArgs> CreateCustomFilterEditorRepositoryItem
seealso: []
---
![CreateCustomFilterEditorRepositoryItem](~/images/createcustomfiltereditorrepositoryitem117055.png)

As you can see in the image above, to create a filter, an end-user should select a column, operator and a value. To provide possible values for the selected column, a repository item is created. You can create a custom repository item for a particular column. For instance, you can create a custom repository item that shows possible values for a particular string type column. For this purpose, subscribe to the **CreateCustomFilterEditorRepositoryItem** event and use the event handler's **CreateCustomRepositoryItemEventArgs.Column** and **CreateCustomRepositoryItemEventArgs.RepositoryItem** parameters.

For details on repository items, refer to the [](xref:DevExpress.XtraEditors.Repository.RepositoryItem) topic.

By default, a repository item that represents the selected column in the current Grid List Editor's GridView is set.