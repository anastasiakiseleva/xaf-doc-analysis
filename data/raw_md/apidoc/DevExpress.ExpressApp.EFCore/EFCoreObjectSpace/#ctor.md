---
uid: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.#ctor(DevExpress.ExpressApp.DC.ITypesInfo,DevExpress.ExpressApp.DC.IEntityStore,System.Func{Microsoft.EntityFrameworkCore.DbContext})
name: EFCoreObjectSpace(ITypesInfo, IEntityStore, Func<DbContext>)
type: Constructor
summary: Initializes a new instance of the @DevExpress.ExpressApp.EFCore.EFCoreObjectSpace class with specified settings.
syntax:
  content: public EFCoreObjectSpace(ITypesInfo typesInfo, IEntityStore entityStore, Func<DbContext> createDbContext)
  parameters:
  - id: typesInfo
    type: DevExpress.ExpressApp.DC.ITypesInfo
    description: An [](xref:DevExpress.ExpressApp.DC.ITypesInfo) object that provides access to XAF-related information on business classes.
  - id: entityStore
    type: DevExpress.ExpressApp.DC.IEntityStore
    description: A source of EF Core-related information on business classes.
  - id: createDbContext
    type: System.Func{Microsoft.EntityFrameworkCore.DbContext}
    description: A method that returns @Microsoft.EntityFrameworkCore.DbContext.
seealso: []
---
