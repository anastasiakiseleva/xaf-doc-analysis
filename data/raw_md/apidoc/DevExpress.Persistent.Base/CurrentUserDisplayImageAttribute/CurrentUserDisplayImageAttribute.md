---
uid: DevExpress.Persistent.Base.CurrentUserDisplayImageAttribute
name: CurrentUserDisplayImageAttribute
type: Class
summary: Applied to business classes that implement a [Security System](xref:113366) user. Specifies the name of a property that stores the current user photo or avatar icon. Has effect in the ASP.NET Core Blazor UI only.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Interface)]
    public class CurrentUserDisplayImageAttribute : Attribute
seealso:
- linkId: DevExpress.Persistent.Base.CurrentUserDisplayImageAttribute._members
  altText: CurrentUserDisplayImageAttribute Members
---
[!include[CurrentUserDisplayImageAttribute_example](~/templates/CurrentUserDisplayImageAttribute_example.md)]

The result is demonstrated in the image below:


![Current user image in a Blazor application](~/images/CurrentUserImage_Blazor.png)