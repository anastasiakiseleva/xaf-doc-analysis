---
uid: DevExpress.ExpressApp.Security.ISecurityUserLoginInfo
name: ISecurityUserLoginInfo
type: Interface
summary: Returns and stores information about the authentication provider and its user ID.
syntax:
  content: public interface ISecurityUserLoginInfo
seealso:
- linkId: DevExpress.ExpressApp.Security.ISecurityUserLoginInfo._members
  altText: ISecurityUserLoginInfo Members
---
[!include[security-multiple-auth-types](~/templates/security-multiple-auth-types.md)]

The following example shows how to use the `ISecurityUserLoginInfo` interface to store a user's authentication methods:

# [C# (EF Core)](#tab/tabid-csharp-efcore)
```csharp
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using DevExpress.ExpressApp.ConditionalAppearance;
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.BaseImpl.EF;

[Table("PermissionPolicyUserLoginInfo")]
public class ApplicationUserLoginInfo : BaseObject, ISecurityUserLoginInfo {

    [Appearance("PasswordProvider", Enabled = false, Criteria = "!(IsNewObject(this)) and LoginProviderName == '" + SecurityDefaults.PasswordAuthentication + "'", Context = "DetailView")]
    public virtual string LoginProviderName { get; set; }

    [Appearance("PasswordProviderUserKey", Enabled = false, Criteria = "!(IsNewObject(this)) and LoginProviderName == '" + SecurityDefaults.PasswordAuthentication + "'", Context = "DetailView")]
    public virtual string ProviderUserKey { get; set; }

    [Browsable(false)]
    public virtual Guid UserForeignKey { get; set; }

    [Required]
    [ForeignKey(nameof(UserForeignKey))]
    public virtual ApplicationUser User { get; set; }

    object ISecurityUserLoginInfo.User => User;
}
```
***
