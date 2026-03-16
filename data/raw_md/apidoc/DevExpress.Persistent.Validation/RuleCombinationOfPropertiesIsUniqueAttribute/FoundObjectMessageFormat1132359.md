---
uid: DevExpress.Persistent.Validation.RuleCombinationOfPropertiesIsUniqueAttribute.FoundObjectMessageFormat
name: FoundObjectMessageFormat
type: Property
summary: Gets or sets the format for specifying information on found objects in the validation error message.
syntax:
  content: public string FoundObjectMessageFormat { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string value that can include one variable. This variable will be set to the key property value of the found object.
seealso: []
---
You can format a list of the found objects that is displayed in the Validation Error window for a broken rule. To do this, use the **RuleCombinationOfPropertiesIsUniqueAttribute** attribute's **FoundObjectMessageFormat** parameter. The passed value will be set for the **FoundObjectMessageFormat** property of the Application Model's **Validation** | **Rules** | **Rule** node. So, you can modify the value directly in the Model Editor.

By default, this property is set to _"{0}"_, which returns a list of found objects separated by the symbol that is specified by [RuleCombinationOfPropertiesIsUniqueAttribute.FoundObjectMessagesSeparator](xref:DevExpress.Persistent.Validation.RuleCombinationOfPropertiesIsUniqueAttribute.FoundObjectMessagesSeparator).

When using the [](xref:DevExpress.Persistent.Validation.RuleCombinationOfPropertiesIsUniqueAttribute), the value for the **FoundObjectMessageFormat** property is passed as a named parameter. This means that you do not have to specify it. However, when specifying, use the following format: `FoundObjectMessageFormat = "{0}"`.

If you set an empty string for **FoundObjectMessageFormat**, only text specified by **MessageTemplateCombinationOfPropertiesMustBeUnique** will be displayed in the validation window.

> [!NOTE]
> The list of the found objects is written in the Validation Error window, if you do not specify **CustomMessageTemplate** in code or the [Model Editor](xref:112582).