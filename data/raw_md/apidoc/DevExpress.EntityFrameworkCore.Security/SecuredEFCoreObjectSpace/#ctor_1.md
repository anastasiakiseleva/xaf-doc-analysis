---
uid: DevExpress.EntityFrameworkCore.Security.SecuredEFCoreObjectSpace.#ctor(DevExpress.ExpressApp.DC.ITypesInfo,DevExpress.ExpressApp.DC.IEntityStore,System.Func{Microsoft.EntityFrameworkCore.DbContext},DevExpress.ExpressApp.Security.ISecurityStrategyBase)
name: SecuredEFCoreObjectSpace(ITypesInfo, IEntityStore, Func<DbContext>, ISecurityStrategyBase)
type: Constructor
summary: Initializes a new instance of the @DevExpress.EntityFrameworkCore.Security.SecuredEFCoreObjectSpace class with specified settings.
syntax:
  content: public SecuredEFCoreObjectSpace(ITypesInfo typesInfo, IEntityStore entityStore, Func<DbContext> createDbContext, ISecurityStrategyBase security)
  parameters:
  - id: typesInfo
    type: DevExpress.ExpressApp.DC.ITypesInfo
    description: An [](xref:DevExpress.ExpressApp.DC.ITypesInfo) object that provides access to XAF-related information on business classes.
  - id: entityStore
    type: DevExpress.ExpressApp.DC.IEntityStore
    description: An **IEntityStore** object.
  - id: createDbContext
    type: System.Func{Microsoft.EntityFrameworkCore.DbContext}
    description: A method that returns @Microsoft.EntityFrameworkCore.DbContext.
  - id: security
    type: DevExpress.ExpressApp.Security.ISecurityStrategyBase
    description: The **ISecurityStrategyBase** object that is the [Security Strategy](xref:113366) used in the application.
seealso: []
---
