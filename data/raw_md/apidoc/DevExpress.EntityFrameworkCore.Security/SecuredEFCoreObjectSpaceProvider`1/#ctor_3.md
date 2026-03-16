---
uid: DevExpress.EntityFrameworkCore.Security.SecuredEFCoreObjectSpaceProvider`1.#ctor(DevExpress.ExpressApp.Security.ISelectDataSecurityProvider,Microsoft.EntityFrameworkCore.IDbContextFactory{`0},DevExpress.ExpressApp.DC.ITypesInfo)
name: SecuredEFCoreObjectSpaceProvider(ISelectDataSecurityProvider, IDbContextFactory<TDbContext>, ITypesInfo)
type: Constructor
summary: Initializes a new instance of the @DevExpress.EntityFrameworkCore.Security.SecuredEFCoreObjectSpaceProvider`1 class with specified settings.
syntax:
  content: public SecuredEFCoreObjectSpaceProvider(ISelectDataSecurityProvider selectDataSecurityProvider, IDbContextFactory<TDbContext> dbContextFactory, ITypesInfo typesInfo)
  parameters:
  - id: selectDataSecurityProvider
    type: DevExpress.ExpressApp.Security.ISelectDataSecurityProvider
    description: An object that implements the **ISelectDataSecurityProvider** interface (for example, a @DevExpress.ExpressApp.Security.SecurityStrategyComplex instance).
  - id: dbContextFactory
    type: Microsoft.EntityFrameworkCore.IDbContextFactory{{TDbContext}}
    description: ''
  - id: typesInfo
    type: DevExpress.ExpressApp.DC.ITypesInfo
    description: An [](xref:DevExpress.ExpressApp.DC.ITypesInfo) object that provides access to XAF-related information on business classes.
seealso: []
---
