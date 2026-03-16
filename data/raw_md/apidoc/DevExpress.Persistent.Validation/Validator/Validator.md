---
uid: DevExpress.Persistent.Validation.Validator
name: Validator
type: Class
summary: Provides access to the [Validation Rules](xref:113008) declared in an **XAF** application.
syntax:
  content: public static class Validator
seealso:
- linkId: DevExpress.Persistent.Validation.Validator._members
  altText: Validator Members
- linkType: HRef
  linkId: https://supportcenter.devexpress.com/ticket/details/e1524/xaf-how-to-highlight-invalid-properties-immediately-in-an-invoked-view
  altText: How to use a Validation module to highlight invalid properties of the business object, when its View is shown
- linkId: DevExpress.ExpressApp.SystemModule.ModificationsController.ModificationsHandlingMode
  altText: ModificationsController.ModificationsHandlingMode
---
The **Validator** class exposes a single `DevExpress.Persistent.Validation.Validator.RuleSet` public property. This property returns a [](xref:DevExpress.Persistent.Validation.RuleSet) object representing all the Validation Rules declared in an application. This object's  methods allow you to trigger validation programmatically. To learn how to do this, refer to the following topic: <xref:113010>.
