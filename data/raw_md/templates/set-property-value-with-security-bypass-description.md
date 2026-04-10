In applications with [middle-tier security](xref:404389), you can call this method only from a business object's [IXafEntityObject.OnSaving](xref:DevExpress.ExpressApp.IXafEntityObject.OnSaving) method, otherwise an exception is thrown.

> [!NOTE]
> In applications with middle-tier security, an object's `OnSaving` method is only called on the middle-tier server side. From this method, you can call `SetPropertyValueWithSecurityBypass` to set values of business object properties even if the client application has no access rights for these properties. Thus, you can use this method to securely initialize properties with sensitive data (it is also important that you define access rules to additionally restrict access to these properties for application users).

The following code snippet demonstrates how to use this method to initialize `CreatedBy`, `UpdatedBy`, and `UpdatedOn` properties of a business class.
