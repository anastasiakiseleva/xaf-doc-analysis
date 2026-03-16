---
uid: DevExpress.Persistent.Validation.RuleUniqueValueAttribute.FoundObjectMessageFormat
name: FoundObjectMessageFormat
type: Property
summary: Gets or sets the format for specifying information on found objects with the specified property value in the validation error message.
syntax:
  content: public string FoundObjectMessageFormat { get; set; }
  parameters: []
  return:
    type: System.String
    description: A sting value that can include one variable. This variable will be set to the key property value of the found object.
seealso: []
---
When a **RuleUniqueValue** rule is broken, a list of the found objects is written in the Validation Error window. You can format this list. To do this, use the **RuleUniqueValue** attribute's **FoundObjectMessageFormat** parameter. The passed value will be set for the **FoundObjectMessageFormat** property of the Application Model's **Validation** | **Rules** | **Rule** node. So, you can modify the value directly in the Model Editor.

By default, this property is set to _"{0}"_, which returns a list of found objects separated by the symbol that is specified by [RuleUniqueValueAttribute.FoundObjectMessagesSeparator](xref:DevExpress.Persistent.Validation.RuleUniqueValueAttribute.FoundObjectMessagesSeparator).

When using the [](xref:DevExpress.Persistent.Validation.RuleUniqueValueAttribute), the value for the **FoundObjectMessageFormat** property is passed as a named parameter. This means that you do not have to specify it. However, when specifying, use the following format: `FoundObjectMessageFormat = "{0}"`.

If you set an empty string for **FoundObjectMessageFormat**, only text specified by **MessageTemplateMustBeUnique** will be displayed in the validation window. Neither the text specified by **MessageTemplateFoundObjects** nor a list of the found objects will be displayed.

> [!NOTE]
> The list of the found objects is written in the Validation Error window, if you do not specify **CustomMessageTemplate** in code or the [Model Editor](xref:112582).
