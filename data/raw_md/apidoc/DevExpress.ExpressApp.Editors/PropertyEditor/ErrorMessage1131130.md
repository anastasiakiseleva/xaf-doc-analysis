---
uid: DevExpress.ExpressApp.Editors.PropertyEditor.ErrorMessage
name: ErrorMessage
type: Property
summary: Specifies the message about [validation rules](xref:113008) broken because of the current Property Editor's bound property.
syntax:
  content: public virtual string ErrorMessage { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string value representing the text shown in the Property Editor's tooltip when a validation rule is broken.
seealso:
- linkId: DevExpress.ExpressApp.View.ErrorMessages
---
Validation rules can be applied to a business class. When these rules are broken, the **ErrorMessage** property of the Property Editors that are bound to the failed properties is set to the value of the **RuleMessageTemplate** specified for these rules. The Property Editor whose **ErrorMessage** property value is not empty is highlighted by an Error image, and the tooltip shows the property's value.

Generally, you do not need to use this property. Although, you may use it as a custom feature for the Validation System, or other system. Note that the custom feature should not impede the [Validation](xref:113684) feature.