---
uid: DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Priority
name: Priority
type: Property
summary: Specifies the priority of the conditional appearance rule generated from the current attribute instance. Used when several rules affect the same UI element.
syntax:
  content: public int Priority { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: An integer value specifying the volume of the conditional appearance rule.
seealso:
- linkId: "113286"
---
There can be several conditional appearance rules affecting the UI element specified by [AppearanceAttribute.TargetItems](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.TargetItems). In this instance, the rules are applied according to the volume specified by the **Priority** property. Rules with a higher volume may override changes made by rules with a lower volume.

If the Priority is not specified, a rule that applies customization always has priority over a rule that cancels customization for the same editor.

> [!NOTE]
> **Priority** is ignored for rules that change an item's visibility, **Enabled** state and font style.
> 
> * **Enabled**: _False_ has higher priority than _True_
> * **Visibility**: _Hide_ has higher priority than _ShowEmptySpace_; _ShowEmptySpace_ has higher priority than _Visible_.
> * **FontStyle**: _Regular_ has lowest priority. Other styles are combined by disjunction.

In the following examples, the Category property is displayed in a Maroon font according to the rule from the first example, and the same property is displayed in a Blue font according to the rule from the second example. When both these rules are applied to the Product class, the priority should be set. Here, the rule from the first example has the higher volume (Priority = 2). So, Category is shown in maroon.

**Example 1**

[!include[ConditionalAppearance_ObjectColoredInListView](~/templates/conditionalappearance_objectcoloredinlistview11916.md)]

**Example 2**

[!include[ConditionalFormatting_CategoryColoredInListViewRule](~/templates/conditionalformatting_categorycoloredinlistviewrule11918.md)]

![ConditionalAppearance_Priority](~/images/conditionalappearance_priority116986.png)