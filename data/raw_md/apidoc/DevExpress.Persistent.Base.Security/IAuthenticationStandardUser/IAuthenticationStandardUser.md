---
uid: DevExpress.Persistent.Base.Security.IAuthenticationStandardUser
name: IAuthenticationStandardUser
type: Interface
summary: Declares members implemented by [Security System](xref:113366) user classes that are compatible with the [](xref:DevExpress.ExpressApp.Security.AuthenticationStandard) authentication.
syntax:
  content: public interface IAuthenticationStandardUser
seealso:
- linkId: DevExpress.Persistent.Base.Security.IAuthenticationStandardUser._members
  altText: IAuthenticationStandardUser Members
---
Support this interface in a class used as a Security System User. An example is provided in the [How to: Implement a Custom Base Persistent Class](xref:113325) topic. If you do not want to implement this interface from scratch, inherit the XPO [](xref:DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyUser) or EF Core [](xref:DevExpress.Persistent.BaseImpl.EF.PermissionPolicy.PermissionPolicyUser) class.