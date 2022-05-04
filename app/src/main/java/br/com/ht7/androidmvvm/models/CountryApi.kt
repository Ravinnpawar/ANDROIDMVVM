package br.com.ht7.androidmvvm.models

import io.reactivex.Single
import retrofit2.http.GET

interface CountryApi {
    @GET("all")
    fun all(): Single<List<Country>>

    @GET("all")
    fun some2(): Single<List<Country>>

    @GET("all")
    fun some1(): Single<List<Country>>

    @GET("all")
    fun some4(): Single<List<Country>>

    @GET("all")
    fun some(): Single<List<Country>>
}