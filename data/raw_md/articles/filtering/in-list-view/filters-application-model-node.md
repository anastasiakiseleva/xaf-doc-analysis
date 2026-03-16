---
uid: "112992"
seealso:
- linkId: "403238"
- linkId: "112809"
title: Filters Application Model Node
owner: Ekaterina Kiseleva
---
# Filters Application Model Node

The **Filters** [Application Model node](xref:112580) allows you to add predefined criteria to the built-in **SetFilter** Action. When selecting a criteria in the Action's drop-down window, the current List View is filtered using this criteria.

![Tutorial_UIC_Lesson19_4](~/images/tutorial_uic_lesson19_4115517.png)

Use this technique to filter List Views when you need an end-user to be able to select the required filter. Moreover, the end-users who have access to the Application Model will be able to add or change predefined filters via the [Model Editor](xref:112582).

The **SetFilter** Action is not activated for List Views that have no filters specified in the **Filters** node. In addition, this Action can be activated for root and nested List Views, since the Main Form and Detail Form [Templates](xref:112609) contain the **Filters** [Action Container](xref:112610) that displays this Action. To learn how to display the Filter Action in a pop-up Window, refer to the [Add Actions to a Popup Window](xref:112804) topic.

To customize the **SetFilter** Action's behavior, access it in code. This Action is contained in the [](xref:DevExpress.ExpressApp.SystemModule.FilterController) and can be accessed via its [FilterController.SetFilterAction](xref:DevExpress.ExpressApp.SystemModule.FilterController.SetFilterAction) property.

## Add Filters via the Model Editor
To add items to the **SetFilter** Action, do the following.

* Invoke the context menu for the required [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] | **Filters** node and select the **Add** | **ListViewFilterItem** menu item.
* For the new **Filter** node, specify the **ID**, **Caption** and **Criteria** properties. The **Criteria** value must be specified using the [Criteria Language Syntax](xref:4928). To simplify this task, you can invoke the **Filter Builder** dialog by clicking an ellipsis button (![EllipsisButton](~/images/ellipsisbutton116182.png)) to the right of the **Criteria** value. Within this dialog, you can visually design a criteria expression.
	
	![ModelEditor_SpecialEditors_Criteria](~/images/modeleditor_specialeditors_criteria116847.png)
* Repeat the previous two steps if needed.
* Return to the **Filters** node, specify the default filter via the **CurrentFilter** property, if needed.

## Add Filters in Code
You can add predefined filters in code via the [](xref:DevExpress.ExpressApp.SystemModule.ListViewFilterAttribute). The filters specified via this attribute are added to the **Filters** node of the **ListView** node whose [IModelObjectView.ModelClass](xref:DevExpress.ExpressApp.Model.IModelObjectView.ModelClass) property is set to the class to which the attribute is applied.

[!include[ListViewFilterAttribute_example](~/templates/ListViewFilterAttribute_example.md)]

If you are going to add a complex filter, which is difficult to write as a string, add the [](xref:DevExpress.ExpressApp.SystemModule.IModelListViewFilterItem) Application Model node in code by implementing a [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorUpdater`1) descendant (Generator Updater) for the [](xref:DevExpress.ExpressApp.SystemModule.ModelListViewFiltersGenerator) Nodes Generator:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Model;
using DevExpress.ExpressApp.Model.Core;
using DevExpress.ExpressApp.SystemModule;
//...
public sealed class Module : ModuleBase {
   // ...	
    public override void AddGeneratorUpdaters(ModelNodesGeneratorUpdaters updaters) {
        base.AddGeneratorUpdaters(updaters);
        updaters.Add(new MyFilterUpdater());          
    }
}
public class MyFilterUpdater : ModelNodesGeneratorUpdater<ModelListViewFiltersGenerator> {
    public override void UpdateNode(ModelNode node) {                
        IModelListViewFilters filtersNode = (IModelListViewFilters)node;
        if(((IModelListView)filtersNode.Parent).ModelClass.TypeInfo.Type == 
            typeof(MyBusinessClass)) {
            IModelListViewFilterItem myFilter = 
                filtersNode.AddNode<IModelListViewFilterItem>("MyComplexFilter");
            myFilter.Criteria = "";
            myFilter.Index = 1;
            myFilter.Caption = "My Filter";
            myFilter.Description = "";
            filtersNode.CurrentFilter = myFilter;
        }
    }
}
```

***

To learn about the entire concept of how to extend the Application Model in code, refer to the [Extend and Customize the Application Model in Code](xref:112810) topic.

To learn how to build criteria, refer to the [Ways to Build Criteria](xref:113052) topic.