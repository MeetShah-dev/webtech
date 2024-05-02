import { HttpService } from '@nestjs/axios';
import { Injectable } from '@nestjs/common';
import { firstValueFrom } from 'rxjs';
import axios from "axios"

@Injectable()
export class AdminService {
    constructor(
        private httpService: HttpService
    ) { }
    async addCategory(req, res) {
        let payload = req.body;
        try {
          const response = await firstValueFrom(this.httpService.post(process.env.ADMIN_API + 'addCategory', payload, {
            headers: {
              'Content-Type': 'application/json'
            }
          }));
          return res.json(response.data);
        } catch (e) {
          console.log("error", e)
        }
      }
      async addCategories(req, res) {
        let payload = req.body;
        try {
          const response = await firstValueFrom(this.httpService.post(process.env.ADMIN_API + 'postManyCategories', payload, {
            headers: {
              'Content-Type': 'application/json'
            }
          }));
          return res.json(response.data);
        } catch (e) {
          console.log("error", e)
        }
      }
      async approvePost(req, res) {
        let payload = req.body;
        payload = {
            ...req.body,
            "user_id": req.user.id.toString()
        }
        try {
          const response = await firstValueFrom(this.httpService.put(process.env.ADMIN_API + 'approvePost', payload, {
            headers: {
              'Content-Type': 'application/json'
            }
          }));
          return res.json(response.data);
        } catch (e) {
          console.log("error", e)
        }
      }
      async rejectPost(req, res) {
        let payload = req.body;
        payload = {
            ...req.body,
            "user_id": req.user.id.toString()
        }
        try {
          const response = await firstValueFrom(this.httpService.put(process.env.ADMIN_API + 'rejectPost', payload));
          return res.json(response.data);
        } catch (e) {
          console.log("error", e)
        }
      }
      async postFeedback(req, res) {
        let payload = req.body;
        payload = {
            ...req.body,
            "user_id": req.user.id.toString()
        }
        try {
          const response = await firstValueFrom(this.httpService.post(process.env.ADMIN_API + 'postFeedback', payload));
          return res.json(response.data);
        } catch (e) {
          console.log("error", e)
        }
      }
      //we can test it later
      async deleteComment(req, res) {
        let payload = req.body;
        try {
          const response = await firstValueFrom(this.httpService.delete(process.env.ADMIN_API + 'deleteComment', payload));
          return res.json(response.data);
        } catch (e) {
          console.log("error", e)
        }
      }
      //need to be test later or not working
      async addCategoryBlog(req, res) {
        let payload = req.body;
        try {
          const response = await firstValueFrom(this.httpService.post(process.env.ADMIN_API + 'addCategoryToBlog', payload));
          return res.json(response.data);
        } catch (e) {
          console.log("error", e)
        }
      }
      async getAllCategories(req, res) {
        try {
            const response: any = await axios.get(process.env.ADMIN_API + 'getAllCategories', {
                data: req.body
            })
            return res.json(response.data);
        } catch (e) {
            console.log(e)
        }
    }
    async getAllUsers(req, res) {
        try {
            const response: any = await axios.get(process.env.ADMIN_API + 'getAllUsers', {
                data: req.body
            })
            return res.json(response.data);
        } catch (e) {
            console.log(e)
        } 
    }
    async changeRole(req, res) {
        let payload = req.body;
        try {
          const response = await firstValueFrom(this.httpService.put(process.env.ADMIN_API + 'changeRole', payload));
          return res.json(response.data);
        } catch (e) {
          console.log("error", e)
        }
    }
    async getReadyPosts(req, res) {
      try {
          const response: any = await axios.get(process.env.ADMIN_API + 'getReadyPosts', {
              data: req.body
          })
          return res.json(response.data);
      } catch (e) {
          console.log(e)
      } 
  }
  async getAllMagazines(req, res) {
    try {
        const response: any = await axios.get(process.env.ADMIN_API + 'getAllMagazines', {
            data: req.body
        })
        return res.json(response.data);
    } catch (e) {
        console.log(e)
    } 
}
}
