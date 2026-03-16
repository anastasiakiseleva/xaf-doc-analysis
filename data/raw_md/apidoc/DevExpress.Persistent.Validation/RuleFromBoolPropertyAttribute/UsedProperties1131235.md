---
uid: DevExpress.Persistent.Validation.RuleFromBoolPropertyAttribute.UsedProperties
name: UsedProperties
type: Property
summary: Specifies the names of the properties to be highlighted when the rule generated from the current attribute is broken.
syntax:
  content: public string UsedProperties { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string value that lists the names of the properties that must be highlighted as invalid when the rule is broken. The names must be separated by a comma.
seealso: []
---
Typically, the target property of the [](xref:DevExpress.Persistent.Validation.RuleFromBoolPropertyAttribute) is marked by the **NonPersistent** attribute, because this property is declared to calculate whether the combination of data of the current object is correct. When this property returns **false**, the rule generated from the applied **RuleFromBoolProperty** attribute is broken. In most cases, the target property should be hidden, since it does not mean anything for end-users. However, when the rule is broken, the properties that contain incorrect data must be highlighted so the end-users can correct the data. To highlight the required properties, their names must be passed as the **UsedProperties** parameter in the **RuleFromBoolProperty** attribute.

Since the **UsedProperties** parameter is a named parameter, it is not necessary to pass its value. If you do not pass, the target property is highlighted as an incorrect one. In this instance, the target property must be visible, so that an end-user can understand what data must be corrected.

> [!IMPORTANT]
> * Always define **UsedProperties** for _warning_ and _info_ rules.
> * [!include[RuleFromBoolPropertyNote](~/templates/RuleFromBoolPropertyNote.md)]

To see an example, refer to the [](xref:DevExpress.Persistent.Validation.RuleFromBoolPropertyAttribute) class description. In addition, you can see an example in the **Validation** section of the **FeatureCenter** Demo. This demo is located in the _[!include[PathToFeatureCenter](~/templates/path-to-feature-center.md)]_ folder, by default.
