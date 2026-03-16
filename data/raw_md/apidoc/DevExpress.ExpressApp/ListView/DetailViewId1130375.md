---
uid: DevExpress.ExpressApp.ListView.DetailViewId
name: DetailViewId
type: Property
summary: Specifies the ID of the Detail View which is invoked from the current List View, or displayed together with a ListView.
syntax:
  content: public string DetailViewId { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string value that represents the ID of the Detail View that represents the object selected in the List View.
seealso: []
---
The **DetailViewId** property allows you to set the ID of the required Detail View that will represent the object selected in the List View. If the **DetailViewId** is empty, the actual Detail View to be displayed will be determined based on the type of the object created or edited via the List View. The default DetailView ID is specified by the [IModelClass.DefaultDetailView](xref:DevExpress.ExpressApp.Model.IModelClass.DefaultDetailView) property of a corresponding **BOModel** | **_\<Class\>_** node

A List View is displayed together with a Detail View when the [IModelListView.MasterDetailMode](xref:DevExpress.ExpressApp.Model.IModelListView.MasterDetailMode) property of the appropriate [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] node is set to the [MasterDetailMode.ListViewAndDetailView](xref:DevExpress.ExpressApp.MasterDetailMode.ListViewAndDetailView). In this scenario, the Detail View represents the object currently focused in the List View's List Editor:

![Tutorial_UIC_Lesson17_2](~/images/tutorial_uic_lesson17_2115512.png)

To access the Detail View, use the [ListView.EditView](xref:DevExpress.ExpressApp.ListView.EditView) property.