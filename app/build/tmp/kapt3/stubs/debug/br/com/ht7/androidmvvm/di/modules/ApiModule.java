package br.com.ht7.androidmvvm.di.modules;

import java.lang.System;

@kotlin.Metadata(mv = {1, 1, 16}, bv = {1, 0, 3}, k = 1, d1 = {"\u0000$\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\b\u0007\u0018\u00002\u00020\u0001B\u0005\u00a2\u0006\u0002\u0010\u0002J\b\u0010\u0007\u001a\u00020\bH\u0007J\b\u0010\t\u001a\u00020\nH\u0007R\u000e\u0010\u0003\u001a\u00020\u0004X\u0082D\u00a2\u0006\u0002\n\u0000R\u000e\u0010\u0005\u001a\u00020\u0006X\u0082.\u00a2\u0006\u0002\n\u0000\u00a8\u0006\u000b"}, d2 = {"Lbr/com/ht7/androidmvvm/di/modules/ApiModule;", "", "()V", "baseUrl", "", "retrofit", "Lretrofit2/Retrofit;", "countryApi", "Lbr/com/ht7/androidmvvm/models/CountryApi;", "countryService", "Lbr/com/ht7/androidmvvm/models/CountryService;", "app_debug"})
@dagger.Module()
public final class ApiModule {
    private final java.lang.String baseUrl = "https://restcountries.eu/rest/v2/";
    private retrofit2.Retrofit retrofit;
    
    @org.jetbrains.annotations.NotNull()
    @dagger.Provides()
    public final br.com.ht7.androidmvvm.models.CountryApi countryApi() {
        return null;
    }
    
    @org.jetbrains.annotations.NotNull()
    @dagger.Provides()
    public final br.com.ht7.androidmvvm.models.CountryService countryService() {
        return null;
    }
    
    public ApiModule() {
        super();
    }
}