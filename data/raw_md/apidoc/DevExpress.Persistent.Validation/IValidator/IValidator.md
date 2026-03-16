---
uid: DevExpress.Persistent.Validation.IValidator
name: IValidator
type: Interface
summary: A service that exposes API required to access the [Validation Rules](xref:113008) declared in an XAF application.
syntax:
  content: public interface IValidator
seealso:
- linkId: DevExpress.Persistent.Validation.IValidator._members
  altText: IValidator Members
- linkId: DevExpress.Persistent.Validation.IRuleSet
- linkType: HRef
  linkId: https://supportcenter.devexpress.com/ticket/details/e1524/xaf-how-to-highlight-invalid-properties-immediately-in-an-invoked-view
  altText: How to use a Validation module to highlight invalid properties of the business object, when its View is shown
- linkType: HRef
  linkId: xref:DevExpress.ExpressApp.SystemModule.ModificationsController.ModificationsHandlingMode
  altText: ModificationsController.ModificationsHandlingMode
---

The `IValidator` service exposes a single [RuleSet](xref:DevExpress.Persistent.Validation.IValidator.RuleSet) public property. This property returns an object that implements the [](xref:DevExpress.Persistent.Validation.IRuleSet) interface. This object contains all Validation Rules declared in an application. The `RuleSet` object's methods allow you to trigger validation programmatically. To learn how to do this, refer to the following topic: <xref:113010>.
