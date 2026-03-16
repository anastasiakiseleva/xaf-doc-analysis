---
uid: DevExpress.ExpressApp.Security.ISecurityUser
name: ISecurityUser
type: Interface
summary: Declares members of a class which is a [Security System](xref:113366) User.
syntax:
  content: public interface ISecurityUser
seealso:
- linkId: DevExpress.ExpressApp.Security.ISecurityUser._members
  altText: ISecurityUser Members
---
Support this interface in a class used as a Security System User. An example is provided in the [How to: Implement a Custom Security System User Based on an Existing Business Class](xref:113452) topic. If you do not want to implement the **ISecurityUser** interface from scratch, inherit the XPO [](xref:DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyUser) or EF Core [](xref:DevExpress.Persistent.BaseImpl.EF.PermissionPolicy.PermissionPolicyUser) class, as demonstrated in the [How to: Implement Custom Security Objects (Users, Roles, Operation Permissions)](xref:113384) topic.