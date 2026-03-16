---
uid: DevExpress.ExpressApp.Win.Editors.WinColumnsListEditor.FilterColumnsMode
name: FilterColumnsMode
type: Property
summary: Specifies whether only properties represented by the List Editor's columns, or all properties, including the properties of the reference properties, are available in the Filter Editor for creating a filter criteria.
syntax:
  content: |-
    [DefaultValue(FilterColumnsMode.AllProperties)]
    public FilterColumnsMode FilterColumnsMode { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Win.Editors.FilterColumnsMode
    description: A **FilterColumnsMode** enumeration value that determines the list of the properties that are available in the Filter Editor of the current Grid List Editor. By default, the **FilterColumnsMode.AllProperties** value is set.
seealso: []
---
The following values are available:

* **FilterColumnsMode.AllProperties** - All properties, including properties of reference properties, are available.
    
    ![FilterColumnsMode_AllProperties](~/images/filtercolumnsmode_allproperties117053.png)
* **FilterColumnsMode.ColumnsOnly** - Only the properties that are represented by columns in the current Grid List Editor are available.
    
    ![FilterColumnsMode_ColumnsOnly](~/images/filtercolumnsmode_columnsonly117054.png)

To specify the required mode for a certain List View, use the following [Controller](xref:112621)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Win.Editors;
// ...
public class CustomizeFilterColumnsModeController : ObjectViewController<ListView, MySolution.Module.BusinessObjects.Person> {
    protected override void OnViewControlsCreated() {
        base.OnViewControlsCreated();
        WinColumnsListEditor listEditor = this.View.Editor as WinColumnsListEditor;
        if (listEditor != null) {
            listEditor.FilterColumnsMode = FilterColumnsMode.ColumnsOnly;
        }
    }
}
```

> [!NOTE]
> When the **Filter Editor** dialog is invoked, the default **StartsWith([**_CurrentColumn_**, ?])** criterion is created automatically (here, _CurrentColumn_ is the column whose header was right-clicked to start the **Filter Editor**). However, if the current column displays a complex property (e.g., **Employee.Department.Office**) and the **FilterColumnsMode** value is **AllProperties**, the **Filter Editor** starts with an empty criterion. This is designed behavior. If you want to autocreate  the default criterion for a complex column, change the **FilterColumnsMode** value to **ColumnsOnly**.