---
uid: DevExpress.Persistent.Base.Security.IAuthenticationActiveDirectoryUser
name: IAuthenticationActiveDirectoryUser
type: Interface
summary: Declares members implemented by a [Security System](xref:113366) user class that is compatible with [](xref:DevExpress.ExpressApp.Security.AuthenticationActiveDirectory) authentication.
syntax:
  content: public interface IAuthenticationActiveDirectoryUser
seealso:
- linkId: DevExpress.Persistent.Base.Security.IAuthenticationActiveDirectoryUser._members
  altText: IAuthenticationActiveDirectoryUser Members
---
Support this interface in a class used as a Security System User. An example is provided in the [How to: Implement a Custom Base Persistent Class](xref:113325) topic. If you do not want to implement this interface from scratch, inherit the XPO [](xref:DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyUser) or EF Core [](xref:DevExpress.Persistent.BaseImpl.EF.PermissionPolicy.PermissionPolicyUser) class.