---
uid: DevExpress.Persistent.Validation.ValidationException
name: ValidationException
type: Class
summary: Occurs if the validation of an `IRuleSet` is unsuccessful.
syntax:
  content: 'public class ValidationException : Exception, IUserFriendlyException'
seealso:
- linkId: DevExpress.Persistent.Validation.ValidationException._members
  altText: ValidationException Members
---
This exception may be triggered by the [IRuleSet.Validate](xref:DevExpress.Persistent.Validation.IRuleSet.Validate*) or [IRuleSet.ValidateAll](xref:DevExpress.Persistent.Validation.IRuleSet.ValidateAll*) method. A `ValidationException` object may be passed through the [ValidationCompletedEventArgs.Exception](xref:DevExpress.Persistent.Validation.ValidationCompletedEventArgs.Exception) property.