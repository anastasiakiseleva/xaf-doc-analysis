---
uid: DevExpress.ExpressApp.Model.IModelClass.DefaultListViewMasterDetailMode
name: DefaultListViewMasterDetailMode
type: Property
summary: Specifies whether to display the default Detail View near the current List View. This option affects List Views whose @DevExpress.ExpressApp.Model.IModelObjectView.ModelClass property is set to the corresponding **IModelClass** instance and does not affect lookup List Views.
syntax:
  content: |-
    [DefaultValue(MasterDetailMode.ListViewOnly)]
    MasterDetailMode DefaultListViewMasterDetailMode { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.MasterDetailMode
    description: A [](xref:DevExpress.ExpressApp.MasterDetailMode) enumeration value that specifies whether to display the default Detail View near the current List View.
seealso:
- linkId: "113249"
---
[!include[ListViewAndDetailView_WebNote](~/templates/ListViewAndDetailView_WebNote.md)]

To set this property, open the [Model Editor](xref:112582) and navigate to the **Application** | **BOModel** | _**\<Class>**_ node: 

![The DefaultListViewMasterDetailMode property in the Model Editor](~/images/ModelEditor_DefaultListViewMasterDetailMode.png)

You can also use the [DefaultListViewOptions](xref:DevExpress.ExpressApp.DefaultListViewOptionsAttribute) attribute to allow in-place editing in code (see [Data Annotations in Data Model](xref:112701)).