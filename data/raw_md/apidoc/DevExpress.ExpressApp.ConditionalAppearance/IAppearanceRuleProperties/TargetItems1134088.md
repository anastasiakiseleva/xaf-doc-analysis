---
uid: DevExpress.ExpressApp.ConditionalAppearance.IAppearanceRuleProperties.TargetItems
name: TargetItems
type: Property
summary: Specifies the identifiers of UI elements affected by the conditional appearance rule.
syntax:
  content: |-
    [Required]
    string TargetItems { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string consisting of semicolon separated identifiers of the UI elements affected by the conditional appearance rule.
seealso:
- linkId: "113286"
---
In Detail Views, identifiers, passed to the **TargetItems** property are **Id** property values of the Application Model nodes that correspond to the UI elements (e.g., [](xref:DevExpress.ExpressApp.Model.IModelMember), [](xref:DevExpress.ExpressApp.Model.IModelLayoutItem), [](xref:DevExpress.ExpressApp.Model.IModelAction), etc.). In List Views, these identifiers are property names.

You can specify several UI elements of the type specified via the [IAppearanceRuleProperties.AppearanceItemType](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearanceRuleProperties.AppearanceItemType) property to be affected by the conditional appearance rule. See the possible variants for specifying the **TargetItems** value in the following table:

| Example | Description |
|---|---|
| "TargetElementId" | An identifier of the individual target element. The element with the "TargetElementId" identifier is affected. |
| "TargetElementId1;TargetElementId2" | A semicolon-separated list of target element identifiers. The listed elements are affected. |
| "\*" | An asterisk (\*) wildcard. All elements are affected. |
| "\*;TargetElementId1;TargetElementId2" | An asterisk (\*) wildcard, followed by a semicolon-separated list of target element identifiers. All elements, except for those listed, are affected. |

> [!NOTE]
> You cannot specify "all Actions" via the "\*" wildcard. To specify several Actions, list their identifiers explicitly. When the **AppearanceItemType** is **Action**, the asterisk sign is interpreted as a reference to an Action that has the "\*" identifier.