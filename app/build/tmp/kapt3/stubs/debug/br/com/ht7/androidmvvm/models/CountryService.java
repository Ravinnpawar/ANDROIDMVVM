package br.com.ht7.androidmvvm.models;

import java.lang.System;

@kotlin.Metadata(mv = {1, 1, 16}, bv = {1, 0, 3}, k = 1, d1 = {"\u0000\"\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0005\n\u0002\u0018\u0002\n\u0002\u0010 \n\u0002\u0018\u0002\n\u0000\u0018\u00002\u00020\u0001B\u0005\u00a2\u0006\u0002\u0010\u0002J\u0012\u0010\t\u001a\u000e\u0012\n\u0012\b\u0012\u0004\u0012\u00020\f0\u000b0\nR\u001e\u0010\u0003\u001a\u00020\u00048\u0006@\u0006X\u0087.\u00a2\u0006\u000e\n\u0000\u001a\u0004\b\u0005\u0010\u0006\"\u0004\b\u0007\u0010\b\u00a8\u0006\r"}, d2 = {"Lbr/com/ht7/androidmvvm/models/CountryService;", "", "()V", "api", "Lbr/com/ht7/androidmvvm/models/CountryApi;", "getApi", "()Lbr/com/ht7/androidmvvm/models/CountryApi;", "setApi", "(Lbr/com/ht7/androidmvvm/models/CountryApi;)V", "getCountries", "Lio/reactivex/Single;", "", "Lbr/com/ht7/androidmvvm/models/Country;", "app_debug"})
public final class CountryService {
    @org.jetbrains.annotations.NotNull()
    @javax.inject.Inject()
    public br.com.ht7.androidmvvm.models.CountryApi api;
    
    @org.jetbrains.annotations.NotNull()
    public final br.com.ht7.androidmvvm.models.CountryApi getApi() {
        return null;
    }
    
    public final void setApi(@org.jetbrains.annotations.NotNull()
    br.com.ht7.androidmvvm.models.CountryApi p0) {
    }
    
    @org.jetbrains.annotations.NotNull()
    public final io.reactivex.Single<java.util.List<br.com.ht7.androidmvvm.models.Country>> getCountries() {
        return null;
    }
    
    public CountryService() {
        super();
    }
}