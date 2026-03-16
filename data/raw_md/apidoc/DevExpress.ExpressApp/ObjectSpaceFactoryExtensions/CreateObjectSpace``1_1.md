---
uid: DevExpress.ExpressApp.ObjectSpaceFactoryExtensions.CreateObjectSpace``1(DevExpress.ExpressApp.IObjectSpaceFactory,System.String)
name: CreateObjectSpace<T>(IObjectSpaceFactory, String)
type: Method
summary: Creates an [object space](xref:113707) for the specified business object type in a [multi-tenant application](xref:404436).
syntax:
  content: public static IObjectSpace CreateObjectSpace<T>(this IObjectSpaceFactory objectSpaceFactory, string tenantName)
  parameters:
  - id: objectSpaceFactory
    type: DevExpress.ExpressApp.IObjectSpaceFactory
    description: A service that creates an object space.
  - id: tenantName
    type: System.String
    description: The name of a tenant or `null` to create an object space for [shared business objects](xref:405451).
  typeParameters:
  - id: T
    description: The type for which the method creates an object space.
  return:
    type: DevExpress.ExpressApp.IObjectSpace
    description: An object space for the specified type.
seealso:
- linkId: "405451"
- linkId: "403669"
- linkId: "403861"
- linkId: "113707"
- linkId: "403858"
---
In [multi-tenant applications](xref:404436), the host database can maintain [shared business objects](xref:405451). Tenants can read this data, but cannot modify it. Host UI administrators have complete CRUD control over host and tenant data.

Call the `CreateObjectSpace` method to create an object space to access the following data:

* Tenant business objects from the host account
* Host-shared business objects from a tenant account

Refer to the following help topic for more information: <xref:405451>.

> [!tip]
> In a tenant account, you can use `CreateObjectSpace` methods without the `tenantName` parameter to get the same result.