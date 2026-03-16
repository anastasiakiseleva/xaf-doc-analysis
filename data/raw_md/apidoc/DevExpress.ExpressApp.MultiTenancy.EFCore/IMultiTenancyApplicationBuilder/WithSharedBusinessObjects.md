---
uid: DevExpress.ExpressApp.MultiTenancy.EFCore.IMultiTenancyApplicationBuilder.WithSharedBusinessObjects(System.Type[])
name: WithSharedBusinessObjects(Type[])
type: Method
summary: Registers the specified host business object types as shared data accessible to tenants.
syntax:
  content: IMultiTenancyApplicationBuilder WithSharedBusinessObjects(params Type[] types)
  parameters:
  - id: types
    type: System.Type[]
    description: The types to share.
  return:
    type: DevExpress.ExpressApp.MultiTenancy.EFCore.IMultiTenancyApplicationBuilder
    description: The application builder that processed the action.
seealso:
- linkId: "404436"
- linkId: "405451"
---
In [multi-tenant applications](xref:404436), the host database can maintain [shared business objects](xref:405451). Call the `WithSharedBusinessObjects` method to register the specified host business object types as shared data.

  # [Startup.cs](#tab/tabid-csharp)
  
  ```csharp
  public class Startup { 
      public void ConfigureServices(IServiceCollection services) { 
          // ... 
          builder.AddMultiTenancy() 
              .WithSharedBusinessObjects(typeof(SharedEntityType1), typeof(SharedEntityType2), ...) 
              // ... 
      } 
  } 
  ``` 
  ***

> [!note]
> * Data types associated with shared types must also be registered as shared types. Otherwise, access to associated objects is denied.
> * If an application uses [middle-tier security](xref:404640), the shared data types should be registered on the server and client side.

Refer to the following help topic for details on how to access shared business objects from a tenant: <xref:405451>.