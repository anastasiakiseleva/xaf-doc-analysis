---
uid: DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Visibility
name: Visibility
type: Property
summary: Specifies the visibility of UI elements affected by the conditional appearance rule generated from this attribute instance.
syntax:
  content: public ViewItemVisibility Visibility { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Editors.ViewItemVisibility
    description: A [](xref:DevExpress.ExpressApp.Editors.ViewItemVisibility) enumeration value specifying the visibility of UI elements affected by the conditional appearance rule.
seealso:
- linkId: "113286"
---
The following UI elements can be made invisible/visible:

* Property Editors that are inherited from the [](xref:DevExpress.ExpressApp.Editors.PropertyEditor) class;
* Layout Items, Layout Groups and Tabbed Layout Groups;
* Actions;
* Data columns in `GridListEditor`, `DxGridListEditor`, `TreeListEditor`, and `DxTreeListEditor` when the appearance rule's criterion does not depend on the current object (for example, `1=1` or an expression that uses a [Function Criteria Operator](xref:113307) without referencing the current object's properties). This scenario is described in the [Conditional Appearance Module Overview](xref:113286) topic.

> [!NOTE]
> The `Show` value of the `Visibility` property has effect in List Views only, when it is required to display a column (see the **Show and Hide List View Columns** section of the [Conditional Appearance Module Overview](xref:113286) topic).

You can find many examples in the [Declare Conditional Appearance Rules in Code](xref:113371) topic. 

[!include[<`Appearance` attribute>](~/templates/main-demo-tip.md)]