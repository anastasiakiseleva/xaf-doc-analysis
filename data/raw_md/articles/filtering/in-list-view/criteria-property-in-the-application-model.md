---
uid: "112990"
seealso:
- linkId: "112988"
- linkId: "113052"
- linkId: "4928"
title: Criteria Property in the Application Model
---
# Criteria Property in the Application Model

The **Criteria** property of the [Application Model](xref:112580)'s [](xref:DevExpress.ExpressApp.Model.IModelListView) node allows you to filter List Views using the [Model Editor](xref:112582). This means that end-users who have access to the Application Model will be able to change this property. However, there will not be a capability to do this without the Model Editor. This topic explains how to use this property.

Use a List View node's **Criteria** property to specify a filtering criteria that will be applied to the current List View. You can use the **Filter Builder** dialog to visually design the required expression. To invoke this dialog, click the ellipsis button (![EllipsisButton](~/images/ellipsisbutton116182.png)) to the right of the property value.

![ModelEditor_SpecialEditors_Criteria_2](~/images/modeleditor_specialeditors_criteria_2116851.png)

The value of this property is added to the **Criteria** collection of the List View's [ListView.CollectionSource](xref:DevExpress.ExpressApp.ListView.CollectionSource). This is performed when the [](xref:DevExpress.ExpressApp.SystemModule.FilterController) is activated. So, if you deactivate this Controller, the **Criteria** property will not be considered for any List View.

This approach can be applied to any List View, whether it is a root, nested in a Lookup Property Editor's drop-down window, or a Link Action's pop-up window - any List View that you can find in the Application Model.

> [!NOTE]
> [!include[CollectionSourceCriteriaNested](~/templates/collectionsourcecriterianested111748.md)]